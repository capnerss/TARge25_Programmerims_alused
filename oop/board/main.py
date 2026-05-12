from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional


@dataclass
class OrderItem:
    """Kirjeldab ühte tellimuse rida."""
    customer: str
    name: str
    quantity: int
    one_item_volume: int

    @property
    def total_volume(self) -> int:
        """Kogu tellimuse rea maht kuupsentimeetrites."""
        return self.quantity * self.one_item_volume


@dataclass
class Order:
    """Kirjeldab ühte tellimust, mis koosneb tellimuse ridadest."""
    order_items: List[OrderItem]
    destination: Optional[str] = None

    @property
    def total_quantity(self) -> int:
        """Kõigi tellimuse ridade summaarne kogus."""
        return sum(item.quantity for item in self.order_items)

    @property
    def total_volume(self) -> int:
        """Kõigi tellimuse ridade summaarne maht."""
        return sum(item.total_volume for item in self.order_items)


@dataclass
class Container:
    """Kirjeldab konteinerit, mis hoiab endas tellimusi."""

    volume: int
    # Kasutame field(default_factory=list), et igal uuel konteineril oleks isiklik tühi nimekiri
    orders: List[Order] = field(default_factory=list)

    @property
    def volume_left(self) -> int:
        """Kui palju ruumi on veel kasutamata."""
        return self.volume - sum(order.total_volume for order in self.orders)


class OrderAggregator:
    """Korjab tellimuse read kokku ja vormistab neist tellimused."""

    def __init__(self):
        self.order_items: List[OrderItem] = []

    def add_item(self, item: OrderItem) -> None:
        """Lisab tellimuse rea agregaatorisse."""
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int) -> Order:
        """Loob etteantud kliendile tellimuse, jälgides mahu ja koguse piiranguid."""
        aggregated_items = []
        remaining_items = []

        current_qty = 0
        current_vol = 0

        # Käime kõik read algses järjekorras läbi
        for item in self.order_items:
            # Kontrollime, kas rida on õigele kliendile ja kas see mahub veel tellimusse
            if item.customer == customer:
                if (current_qty + item.quantity <= max_items_quantity) and \
                        (current_vol + item.total_volume <= max_volume):

                    aggregated_items.append(item)
                    current_qty += item.quantity
                    current_vol += item.total_volume
                else:
                    # Kui ei mahu, siis jääb ootele
                    remaining_items.append(item)
            else:
                # Teiste klientide read jäävad samuti ootele
                remaining_items.append(item)

        # Uuendame agregaatori nimekirja (lisatud read on nüüd eemaldatud)
        self.order_items = remaining_items

        return Order(aggregated_items)


class ContainerAggregator:
    """Vastutab valmis tellimuste konteineritesse jagamise eest sihtkohtade kaupa."""

    def __init__(self, container_volume: int):
        """Kõigi tellimuse ridade summaarne kogus."""
        self.container_volume = container_volume
        self.not_used_orders: List[Order] = []

    def prepare_containers(self, orders: Tuple[Order, ...]) -> Dict[str, List[Container]]:
        """Loob ning paneb tellimused konteineritesse."""
        destinations: Dict[str, List[Container]] = {}

        for order in orders:
            # Kui tellimus on üksinda juba suurem kui konteineri maksimaalne maht,
            # ei mahu see kunagi kuhugi ja läheb not_used_orders nimekirja.
            if order.total_volume > self.container_volume:
                self.not_used_orders.append(order)
                continue

            dest = order.destination
            # Kui sihtkohta pole veel sõnastikus, loome sellele tühja nimekirja
            if dest not in destinations:
                destinations[dest] = []

            placed = False
            # Otsime olemasolevatest selle sihtkoha konteineritest sobivat
            for container in destinations[dest]:
                if container.volume_left >= order.total_volume:
                    container.orders.append(order)
                    placed = True
                    break

            # Kui ükski olemasolev konteiner ei sobinud (või neid veel polnud), loome uue
            if not placed:
                new_container = Container(self.container_volume)
                new_container.orders.append(order)
                destinations[dest].append(new_container)

        return destinations
