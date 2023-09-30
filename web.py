import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"   #write string from textbox to local variable
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Dennis' Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] #delete item from dictionary 'st.session_state'
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#print("Hello")
#st.session_state
