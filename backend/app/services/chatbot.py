from app.services.intent import detect_intent
from app.models.order import Order
from app.models.chat import Chat
from app.db.db_dependency import get_db

def handle_chat(user_id, message, db):

    intent = detect_intent(message)

    response = ""

    if intent == "order_status":

        order = ( 
        db.query(Order)
        .filter(Order.user_id == user_id)
        .first()
        )

        if order:
            response = (
                f"Your order status is '{order.status}'"
                f" and it is expected to be delivered by {order.delivery_date}."
            )

        else:
            response = "I couldn't find any orders associated with your account."

    elif intent == "refund":

        response = (
            "Refunds are processed within 5-7 business days."
        )

    elif intent == "customer_support":

        response = (
            "Our customer support team is available 24/7. "
            "You can reach us at support@company.com."
        )

    else:

        response = (
            "I'm here to help! You can ask about your order status, "
            "refunds, or contact customer support."
        )

    
    chat_history = Chat(
        user_id=user_id,
        message=message,
        response=response,
        intent=intent
    )

    db.add(chat_history)
    db.commit()

    return {
        "intent": intent,
        "response": response
    }
