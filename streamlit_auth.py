import streamlit as st
from streamlit_auth import gmail_login
from googleapiclient.errors import HttpError

st.title("📧 Gmail Analytics Studio")

service = gmail_login()

if service:
    try:
        # Sample: Get number of emails
        profile = service.users().getProfile(userId='me').execute()
        total_messages = profile.get('messagesTotal')
        st.metric("Total Emails", total_messages)

        # Sample: List latest 5 threads
        results = service.users().threads().list(userId='me', maxResults=5).execute()
        threads = results.get('threads', [])

        st.subheader("Recent Threads:")
        for thread in threads:
            data = service.users().threads().get(userId='me', id=thread['id']).execute()
            snippet = data.get('snippet', '')
            st.write(snippet)
    except HttpError as e:
        st.error(f"An error occurred: {e}")
