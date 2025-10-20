import streamlit as st
from agent import agentic_search

def agentic_search(query):
    return f"Agent's response to your query: {query}"

def main():
    st.title("Marketplace Sellers' Agent")

    st.write("Enter your query to get assistance from the agent.")

    user_query = st.text_area("Your query")

    if st.button("Submit"):
        if user_query.strip() == "":
            st.warning("Please enter a query.")
        else:
            with st.spinner("Processing..."):
                response = get_agent_response(user_query)
            st.markdown("### Agent's Response")
            st.write(response)

if __name__ == "__main__":
    main()