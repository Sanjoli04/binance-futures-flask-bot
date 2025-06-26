from flask import jsonify,request, abort
import logging
def register_routes(app,bot):
    ##################### ===== ERROR HANDLERS ===== ####################
    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify({"error": str(error)})
        response.status_code = 500
        return response

    @app.errorhandler(404)
    def page_not_found_error(error):
        response = jsonify({'error': str(error)})
        response.status_code = 404
        return response

    @app.errorhandler(422)
    def unprocessable_entity(error):
        response = jsonify({'error': str(error)})
        response.status_code = 422
        return response

    ################################# ==== ROUTES ==== ################################
    @app.get("/")
    def home():
        return jsonify({"message": "The Trading bot is running."})
    @app.post("/place-order")
    def place_order():
        logging.info("/place-order hit")
        data = request.get_json()
        if not data.get("symbol"):
            abort(422, description="symbol can't be found in payload sent.")    
        if not data.get("side"):
            abort(422, description="side can't be found in payload sent.")    
        if not data.get("type"):
            abort(422, description="type can't be found in payload sent.")    
        if not data.get("quantity"):
            abort(422, description="quantity can't be found in payload sent.")    

        try:
            ## Place order
            response = bot.create_order(**data)
            return jsonify({"message": "Order placed Successfully","order": response}),200
        except Exception as e:
            logging.error(f"Order failed: {e}")
            abort(500, description="Order placement failed due to a server error.")

    @app.get("/account-balance")
    def get_balance():
        ## Now get the futures account balance
        logging.info("/account-balance hit")
        try:
            account_balance = bot.get_balance()
            return jsonify(account_balance),200
        except Exception as e:
            logging.error(f"Failed to fetch futures account balance: {e}")
            abort(500, description="Could not retrieve account balance due to a server error.")

    @app.get("/position")
    def get_position():
        logging.info("/position hit")
        try:
            position = bot.get_position_info()
            return jsonify(position),200
        except Exception as e:
            logging.error(f"Failed to fetch position information: {e}")
            abort(500,description="Could not retrieve position information due to server error.")
    @app.delete("/cancel-order")
    def cancel_order():
        logging.info("/cancel-order hit")
        if not request.args.get("order_id"):
            abort(422, description="order_id is not found in payload sent.")
        if not request.args.get("symbol"):
            abort(422, description="symbol is not found in payload sent.")
        try:
            order_id=int(request.args.get("order_id"))
            symbol=request.args.get("symbol")
            bot.cancel_order(order_id=order_id,symbol=symbol)
            return jsonify({ "message": "Future order cancelled with order id {} and symbol {}".format(order_id,symbol)}),200
        except Exception as e:
            logging.error(f"Failed to cancel the order: {e}")
            abort(500, description="Couldn't cancel the order due to server error.")
