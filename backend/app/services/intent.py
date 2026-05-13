def detect_intent(message: str) -> str:
    
    if "order" in message.lower():
        return "order_status"
    elif "refund" in message.lower():
        return "refund"
    elif "support" in message.lower():
        return "customer_support"
    else:
        return "general"