import streanlit as st
st.title("Asistente Virtual")

if "Messages" not in st.session_state:
    st.session_state.messages=[]
if "First_mensaje" not in st.session_state:
    st.session_state.first_mensaje= True

for message in st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown("Hola,¿Como puedo ayudarte?")
        
    st.session_state.messages.append({"role" : "assistant", "content" :"Hola,¿Como puedo ayudarte?"})
    st.session.state.first_message= False

if prompt  := st.chatinput("¿Como puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.message.append({"role" : "user", "content" : prompt})
    
    with st.chat_message("assistan"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role" : "assistan" , "content" : prompt})
    