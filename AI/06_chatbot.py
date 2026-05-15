def blinkit_chatbot():
    print("=== Welcome to Blinkit Chatbot ===")

    while True:
        user = input("\nYou: ").lower()

        # Greeting
        if user == "hello" or user == "hi":
            print("Bot: Hello! How can I help you today?")
            print("Bot: You can ask about orders, delivery, payment, or offers.")

        # Order Section
        elif user == "order":
            print("Bot: What do you want to know?")
            print("1. Track Order")
            print("2. Cancel Order")

            choice = input("Enter choice: ").lower()

            # Nested if
            if choice == "1" or choice == "track order":
                print("Bot: Your order is on the way and will arrive in 10 minutes.")

            elif choice == "2" or choice == "cancel order":
                print("Bot: Your order has been cancelled successfully.")

            else:
                print("Bot: Invalid order option.")

        # Delivery Section
        elif user == "delivery":
            city = input("Bot: Enter your city: ").lower()

            # Nested condition
            if city == "pune":
                print("Bot: Delivery available in 10 minutes.")

            elif city == "mumbai":
                print("Bot: Delivery available in 15 minutes.")

            else:
                print("Bot: Sorry, service is not available in your city.")

        # Payment Section
        elif user == "payment":
            print("Bot: Available payment methods:")
            print("- UPI")
            print("- Debit/Credit Card")
            print("- Cash on Delivery")

        # Offers Section
        elif user == "offers":
            member = input("Bot: Are you a premium member? (yes/no): ").lower()

            # Nested if
            if member == "yes":
                print("Bot: You get 30% discount and free delivery!")

            else:
                print("Bot: You get 10% discount on groceries.")

        # Help Section
        elif user == "help":
            print("Bot: Available commands:")
            print("hello, order, delivery, payment, offers, bye")

        # Exit
        elif user == "bye":
            print("Bot: Thank you for using Blinkit Chatbot!")
            break

        # Default
        else:
            print("Bot: Sorry, I don't understand your request.")


# Run chatbot
blinkit_chatbot()





















# import streamlit as st

# bot_name = "College Buddy"

# knowledge_base = {

#     "what is your name?" : [
#         f"My name is {bot_name}! \n Happy to help you out with your College enquiries!"
#     ],

#     "hello": [
#         f"Hello my name is {bot_name}! \n Happy to help you out with your College enquiries!"
#     ],

#     "what are the best colleges from pune?": [
#         "COEP",
#         "PICT",
#         "VIT",
#         "CUMMINS",
#         "PCCOE"
#     ],

#     "which are the best engineering branches?" : [
#         "Computer Engineering",
#         "IT Engineering",
#         "ENTC Engineering"
#     ],

#     "what are the top branch cut-offs for coep?" : [
#         "Computer Engineering : 99.8 percentile",
#         "Does not have IT branch",
#         "ENTC Engineering: 99.2 percentile",
#     ],   

#     "what are the top branch cut-offs for pict?" : [
#         "Computer Engineering : 99.4 percentile",
#         "IT Engineering : 98.6 percentile",
#         "ENTC Engineering: 97.2 percentile",
#     ],  

#     "what are the top branch cut-offs for vit?" : [
#         "Computer Engineering : 99.8 percentile",
#         "IT Engineering: 97.1 percentile",
#         "ENTC Engineering: 96.2 percentile",
#     ],    

#     "what are the top branch cut-offs for cummins?" : [
#         "Computer Engineering : 99.8 percentile",
#         "Does not have IT branch",
#         "ENTC Engineering: 99.2",
#     ],  

#     "what are the top branch cut-offs for pccoe?" : [
#         "Computer Engineering : 99.8 percentile",
#         "Does not have IT branch",
#         "ENTC Engineering: 99.2",
#     ], 

#     "When do college admissions start?": [
#         "Admissions generally start around August",
#     ],
   
# }

# st.header("College Enquiry Rule Based Chatbot")

# def respond(input: str):
#     if (input in knowledge_base):
#         print(input)
#         values = knowledge_base[input]
#         for value in values:
#             st.write(value)
#     else:
#         print(input)
#         key = input
#         st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
#         answer = st.text_input("Answer")
#         add = st.button("Add answer")
#         if (add):
#             knowledge_base[key] = [answer]

# if __name__ == "__main__":
#     input = st.text_input("Enter a query here-")
#     input = input.lower()
#     col1, col2 = st.columns([1,0.1])
#     with col1:
#         ask = st.button("Ask")
#     with col2:
#         quit = st.button("Quit")
#     if (ask):
#         respond(input)
#     if (quit):
#         st.write("Thank you for using the Chatbot")
    
