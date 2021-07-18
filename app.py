import streamlit as st
from datetime import datetime

try:
    st.set_page_config(
        page_title='The Starbucks Web Store',
        page_icon='https://cdn.iconscout.com/icon/free/png-256/starbucks-226353.png'
    )
except:
    pass

st.image('https://www.nestleprofessionalmena.com/sites/site.prod.nestleprofessionalmena.com/files/banners/MainBanner_1288x411_1.jpg')
st.title('Starbucks: Web App')
st.text('Description: this is a web-based order-taking app for Starbucks!')
st.text('May I take your order?')

prices = {
    'Cafe Americano': {
        'Short': 3_500,
        'Tall': 4_500,
        'Grande': 5_500,
        'Venti': 6_500,
    },
    'Cafe Latte': {
        'Short': 3_750,
        'Tall': 4_750,
        'Grande': 5_750,
        'Venti': 6_750,
    },
}

menu = st.selectbox('Select something from the menu', ('Cafe Americano', 'Cafe Latte'))
size = st.selectbox('What size?', ('Short', 'Tall', 'Grande', 'Venti'))
quantity = st.selectbox('How many cups?', (n for n in range(1, 11)))

add_shot = st.checkbox('Add shot?')
add_options = st.multiselect(
    'Additional options (select multiple)',
    ('Option A', 'Option B', 'Option C')
)
add_special_option = st.radio(
    'Additional special options (select one)',
    ('Add milk', 'Add syrup', 'Add cream')
)
hot_cold = st.radio('Hot or cold?', ('Hot', 'Cold'))

if hot_cold == 'Hot':
    temp = st.slider('Exact temperature', min_value=60, max_value=100, step=1)
    st.text(f'Okay, we will prepare your coffee at {temp} degrees celsius')

add_requests = st.text_input('Is there anything else we should know?')

satisfaction = st.select_slider(
    'Please tell us your satisfaction level',
    options=('Angry', 'Annoyed', 'Whatever', 'Happy', 'So Happy')
)

tip = st.number_input('How much tip would you like to give?', min_value=0, max_value=10_000, step=1_000)

price = prices[menu][size]
total = price * quantity

d = st.date_input('When can you pick up you order?', datetime.now())
t = st.time_input('At what time?', datetime.now())

st.markdown(f'''
# Current Order
### Menu: {menu} ({size}) x {quantity}
### Total: ₩{price} x {quantity} = `₩{total}`
{'### Additional requests: ' + add_requests if add_requests else ''}
{'### Tip: ₩' + str(tip) if tip else ''}
### Today, you are feeling `{satisfaction}`
''')

st.title('Here is the code')

code = '''
price = prices[menu][size]
total = price * quantity
'''
st.code(code, language='python')

st.title('Place an order?')

my_table = None

def place_order():
    # pretend that this function makes a request to some
    # server out in the cloud
    print('---New order---')
    print('menu:', menu)
    print('size:', size)
    print('quantity:', quantity)

if st.button('Place my order', on_click=place_order):
    st.title('Your order has been placed!')
    st.image('https://image.slidesharecdn.com/presentation-150429012118-conversion-gate01/95/how-and-why-a-global-brand-starbucks-failed-in-australia-22-638.jpg')


# Here is the link to the streamlit api
# https://docs.streamlit.io/en/stable/api.html
