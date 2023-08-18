import streamlit as st 
from processButton import get_pdf_text ,get_vectorstore ,get_text_chunks ,get_conversation_chain


def main():
    st.set_page_config(page_title="Chat with multiple files",page_icon=":books:")
    
    st.header("Chat with multiple PDF's")    
    user_question = st.text_input("Ask a question about your document:")
    
    
    
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
               
                
                # create vector store
                vectorstore = get_vectorstore(text_chunks)
                st.write(vectorstore)
        
                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                  vectorstore)
        
        
if __name__ == "__main__":
    main()        
