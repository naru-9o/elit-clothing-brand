from flask import Flask,request,render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Text, nullable=False)  # Store cart items as a JSON string
    total_price = db.Column(db.Float, nullable=False)

    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

    

with app.app_context():
    db.create_all()



@app.route('/')
def web():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']


        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['name'] = user.name
            session['email'] = user.email  
            return redirect('/home')
        else:
            return render_template('login.html',error= 'Invalid user')
        
    return render_template('login.html')


@app.route('/home')
def home():
    if session['name']:
        return render_template('index.html')
    
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')

@app.route('/Men-shop')
def shop():
    products_page3 = [
        {
            "id": 1,
            "name": "Dior Oblique Puffer Overshirt",
            "description": "Black Technical Jacquard",
            "image1": "images/img7.webp",
            "image2": "images/img7.1.webp",
            "link": "/Mstore"
        },
        {
            "id": 2,
            "name": "East-West Tote Bag",
            "description": "Black Dior Oblique Jacquard and Black Grained Calfskin",
            "image1": "images/img8.webp",
            "image2": "images/img8.1.webp",
            "link": "/Mstore"
        }
    ]

    products_page4 = [
        {
            "id": 3,
            "name": "Cropped Jacket",
            "description": "Gray Felted Cashmere and Virgin Wool",
            "image1": "images/img9.webp",
            "image2": "images/img9.1.webp",
            "link": "/Mstore"
        },
        {
            "id": 4,
            "name": "Christian Dior Couture Bomber Jacket",
            "description": "Brown Calfskin",
            "image1": "images/img10.webp",
            "image2": "images/img10.1.webp",
            "link": "/Mstore"
        },
        {
            "id": 5,
            "name": "Zipped Jacket",
            "description": "Gray Virgin Wool Twill",
            "image1": "images/img11.webp",
            "image2": "images/img11.1.webp",
            "link": "/Mstore"
        }
    ]
    return render_template('shop.html', products_page3 = products_page3, products_page4 = products_page4)





@app.route('/Women-shop')
def wshop():
    w_product = [
            {
        "id": 6,
        "name": "Miss Montaigne Mini Bag",
        "description": "Blue Dior Oblique Jacquard",
        "image1": "images/img12.1.webp",
        "image2": "images/img12.avif",
        "link": "/wstore"
    },
    {
        "id": 7,
        "name": "30 Montaigne Avenue Double Carry Mini Bag",
        "description": "Blue Dior Oblique Jacquard and Smooth Calfskin",
        "image1": "images/img13.webp",
        "image2": "images/img13.1.webp",
        "link": "/wstore"
    },
    {
        "id": 8,
        "name": "Medium DiorTravel Nomad Pouch",
        "description": "Blue Denim Dior Oblique Jacquard",
        "image1": "images/img14.webp",
        "image2": "images/img14.1.avif",
        "link": "/wstore"
    }

    ]
    return render_template('wshop.html', w_product = w_product)





@app.route('/Mstore')
def mstore():
    m_store = [
        {
        "id": "Black Technical Jacquard",
        "name": "Dior Oblique Puffer Overshirt",
        "description": "The puffer overshirt pays tribute to the House's hallmark Dior Oblique motif. Crafted in lightweight black technical jacquard, it stands out with a Dior rubber patch on the back and a patch pocket on the chest.",
        "price": 1300,
        "image1": "images/img7.webp",
        "image2": "images/img7.1.webp",
        "image3": "images/img7.2.webp" 
    },
    ]

    m1_store = [
            {
        "id": "Black Dior Oblique Jacquard and Black Grained Calfskin",
        "name": "East-West Tote Bag",
        "description": "The East-West tote bag is a refined and timeless style. The silhouette is crafted in black Dior Oblique jacquard, offering a new take on the iconic House motif, and is enhanced by tonal grained calfskin.",
        "price": 1500,
        "image1": "images/img8.webp",
        "video": "videos/man-video2.mp4",
        "image2": "images/img8.1.webp"
    },

    {
        "id": "Gray Felted Cashmere and Virgin Wool",
        "name": "Cropped Jacket",
        "description": "Tailoring is quintessential Dior atelier savoir-faire and lies at the heart of House heritage. The cropped jacket in gray felted cashmere and virgin wool celebrates this unique expertise.",
        "price": 12000,
        "image1": "images/img9.webp",
        "video": "videos/man-video3.mp4",
        "image2": "images/img9.1.webp"
    },
    {
        "id": "Brown Calfskin",
        "name": "Christian Dior Couture Bomber Jacket",
        "description": "Unveiled at the Winter 2024 Fashion Show, the bomber jacket is both modern and timeless. Made in brown calfskin, it is enhanced by a debossed Christian Dior Couture signature on the chest as well as side welt pockets and gussets on the rear.",
        "price": 6000,
        "image1": "images/img10.webp",
        "video": "videos/man-video4.mp4",
        "image2": "images/img10.1.webp"
    }
]


    return render_template('mstore.html', m_store = m_store, m1_store = m1_store)



@app.route('/wstore')
def wstore():
    w_store = [
            {
        "id": "Blue Dior Oblique Jacquard",
        "name": "Miss Montaigne Mini Bag",
        "description": "New for Winter 2024, the 30 Montaigne Avenue East-West Double Carry mini bag is both contemporary and refined. Constructed in blue Dior Oblique jacquard, it has a tonal smooth calfskin flap embellished with an antique gold-finish metal CD twist clasp inspired by the seal of a Christian Dior.",
        "price": 1600,
        "image1": "images/img12.1.webp",
        "image2": "images/img12.2.webp",
        "image3": "images/img12.avif"
        },
    ]

    w1_store = [
    {
        "id": "Blue Dior Oblique Jacquard and Smooth Calfskin",
        "name": "30 Montaigne Avenue Double Carry Mini Bag",
        "description": "New for Winter 2024, the Miss Montaigne mini bag is a practical and elegant style. Crafted in blue Dior Oblique jacquard, it features a flap embellished with an antique gold-finish metal CD twist clasp inspired by the seal of a Christian Dior perfume bottle.",
        "price": 1700,
        "image1": "images/img13.webp",
        "video": "videos/woman-video1.mp4",
        "image2": "images/img13.1.webp"
    },
    {
        "id": "Blue Denim Dior Oblique Jacquard",
        "name": "Medium DiorTravel Nomad Pouch",
        "description": "The Diorstar hobo bag with chain has a practical, modern look. Crafted in blue denim, it features the Graphic Cannage motif, offering a modern and 3D twist on the House icon, and has a supple silhouette and spacious compartment.",
        "price": 1900,
        "image1": "images/img14.webp",
        "video": "videos/woman-video2.mp4",
        "image2": "images/img14.2.webp"
    }
]


    return render_template('wstore.html', w_store = w_store, w1_store = w1_store)



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    product_data = request.json
    print('Received product data:', product_data)  # Debugging line

    if product_data:
        # Initialize the cart if it doesn't exist
        session['cart'] = session.get('cart', [])
        cart = session['cart']

        # Check if the product is already in the cart
        for item in cart:
            if item['name'] == product_data['name']:  # Match by 'name' or another unique identifier
                item['quantity'] += 1  # Increment the quantity
                session.modified = True  # Mark session as modified
                print('Updated product quantity:', item)  # Debugging line
                break
        else:
            # If product not found, add it with a quantity of 1
            product_data['quantity'] = 1
            cart.append(product_data)
            session.modified = True  # Mark session as modified
            print('Added new product to cart:', product_data)  # Debugging line

        return {'success': True, 'cart': cart}
    else:
        return {'success': False, 'message': 'No product data received'}


    
@app.route('/remove-from-cart/<int:index>', methods=['POST'])
def remove_from_cart(index):
    print('Removing item at index:', index)  # Debugging line
    cart = session.get('cart', [])
    if 0 <= index < len(cart):
        cart.pop(index)  # Remove the item at the given index
        session['cart'] = cart  # Update the cart in the session
        print('Updated cart:', cart)  # Debugging line
        return {'success': True}
    print('Index out of range:', index)  # Debugging line
    return {'success': False}



@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    
    # Calculate total price in the backend
    total_price = 0
    try:
        total_price = sum(
            float(item['price'].replace('$', '').replace(',', '')) * item.get('quantity', 1)
            for item in cart_items
        )
    except ValueError as e:
        print(f"Error calculating total price: {e}")  # Log any conversion errors

    # Query the latest order (if any)
    order = Order.query.order_by(Order.id.desc()).first()

    return render_template('cart.html', cart_items=cart_items, total_price=total_price, order=order)



@app.route('/place_order', methods=['POST'])
def place_order():
    cart_items = session.get('cart', [])

    if not cart_items:
        flash("Your cart is empty. Please add some products before ordering.", "error")
        return redirect(url_for('cart'))

    # Calculate total price again just to be sure
    total_price = 0
    try:
        total_price = sum(float(item['price'].replace('$', '').replace(',', '')) for item in cart_items)
    except ValueError as e:
        print(f"Error calculating total price: {e}")

    # Save order in the database
    new_order = Order(items=str(cart_items), total_price=total_price)
    db.session.add(new_order)
    db.session.commit()

    # Flash a success message
    flash("Your order has been placed successfully!", "success")
    
    # Redirect back to the cart page
    return redirect(url_for('cart'))





@app.route('/cancel_order/<int:order_id>', methods=['POST'])
def cancel_order(order_id):
    # Query the order based on the ID
    order_to_cancel = Order.query.get(order_id)
    
    if order_to_cancel:
        # Remove the order from the database
        db.session.delete(order_to_cancel)
        db.session.commit()
        
        # Flash a success message
        flash("Your order has been canceled.", "success")
    else:
        # Flash an error message if the order is not found
        flash("Order not found.", "error")
    
    # Redirect the user back to the cart or order page
    return redirect(url_for('cart'))





@app.route('/clear_cart', methods=['POST'])
def clear_cart():
    # Clear the cart from the session
    session.pop('cart', None)
    flash("Your cart has been cleared.", "success")
    
    # Redirect back to the cart page
    return redirect(url_for('cart'))




if __name__ == "__main__":
    app.run(debug=True)