const express = require('express');
const mongoose = require('mongoose');
const session = require('express-session');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Kết nối đến MongoDB
mongoose.connect('mongodb://localhost:27017/products_database', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => console.log('Connected to MongoDB'));

// Cấu hình session
app.use(session({
    secret: 'yourSecretKey',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 30 * 60 * 1000 } // Session timeout 30 phút
}));

// Định nghĩa mô hình Product
const productSchema = new mongoose.Schema({
    name: String,
    category: String,
    price: Number,
    description: String,
    images: [String]
});

const Product = mongoose.model('Product', productSchema);

// API lấy danh sách sản phẩm
app.get('/api/products', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

// API thêm sản phẩm vào giỏ hàng
app.post('/api/cart/add', (req, res) => {
    const { productId, quantity } = req.body;

    if (!req.session.cart) {
        req.session.cart = [];
    }

    const existingProductIndex = req.session.cart.findIndex(item => item.productId === productId);

    if (existingProductIndex >= 0) {
        req.session.cart[existingProductIndex].quantity += quantity;
    } else {
        req.session.cart.push({ productId, quantity });
    }

    res.json({ cart: req.session.cart });
});

// API lấy thông tin giỏ hàng
app.get('/api/cart', async (req, res) => {
    if (!req.session.cart) {
        return res.json({ cart: [] });
    }

    const cartItems = await Promise.all(req.session.cart.map(async (item) => {
        const product = await Product.findById(item.productId);
        return {
            product,
            quantity: item.quantity
        };
    }));

    res.json({ cart: cartItems });
});

// API xóa sản phẩm khỏi giỏ hàng
app.delete('/api/cart/remove', (req, res) => {
    const { productId } = req.body;
    req.session.cart = req.session.cart.filter(item => item.productId !== productId);
    res.json({ cart: req.session.cart });
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));
