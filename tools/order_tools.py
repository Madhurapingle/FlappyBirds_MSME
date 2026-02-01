def create_order(entities: dict) -> dict:
    # placeholder for DB / API call
    return {
        "status": "success",
        "message": "Order created successfully",
        "order_id": "ORD-12345"
    }


def cancel_order(entities: dict) -> dict:
    return {
        "status": "success",
        "message": "Order cancelled successfully"
    }


def fetch_status(entities: dict) -> dict:
    return {
        "status": "success",
        "message": "Order is being processed",
        "order_id": "ORD-12345"
    }
