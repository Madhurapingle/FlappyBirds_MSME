def check_inventory(product: str, quantity: int) -> dict:
    inventory = {
        "laptop": 10,
        "phone": 25
    }

    available = inventory.get(product.lower(), 0)

    return {
        "available": available,
        "requested": quantity,
        "sufficient": available >= quantity
    }


def check_staff(role: str = "packer") -> dict:
    # mock staff availability
    staff = {
        "packer": False,
        "delivery": False
    }

    return {
        "role": role,
        "available": staff.get(role, False)
    }
