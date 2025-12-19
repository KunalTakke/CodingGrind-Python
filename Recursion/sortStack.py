
def sortStack(st):
    if len(st) == 1:
        return 
    
    temp = st.pop()
    sortStack(st)
    insertStack(st)

def insertStack(st,temp):
    if len(st) == 0 or st[-1]<=temp:
        st.append(temp)
        return 
    val = st.pop()
    insertStack(st,temp)
    st.append(val)
    
