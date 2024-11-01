const express = require('express');
const session = require('express-session');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
const PORT = 3000;
const mongoUrl = 'mongodb://localhost:27017';
const dbName = 'products_database';

let db;

// Kết nối MongoDB
MongoClient.connect(mongoUrl, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(client => {
    db = client.db(dbName);
    console.log('Connected to MongoDB');
  })
  .catch(error => console.error(error));

// Cấu hình session
app.use(session({
  secret: 'yourSecretKey',
  resave: false,
  saveUninitialized: true,
}));

app.use(express.json());
app.use(express.static('public')); // Nơi chứa file HTML, CSS, JavaScript

// API lấy danh sách sản phẩm
app.get('/api/products', async (req, res) => {
  const products = await db.collection('Products').find().toArray();
  res.json(products);
});

// API thêm sản phẩm vào giỏ hàng
app.post('/api/cart/add', (req, res) => {
  const { productId, quantity } = req.body;
  const product = { productId, quantity };

  if (!req.session.cart) req.session.cart = [];
  
  // Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
  const existingProduct = req.session.cart.find(item => item.productId === productId);

  if (existingProduct) {
    existingProduct.quantity += quantity; // Tăng số lượng nếu đã tồn tại
  } else {
    req.session.cart.push(product); // Thêm sản phẩm mới
  }
  res.send('Product added to cart');
});

// API lấy chi tiết giỏ hàng
app.get('/api/cart', async (req, res) => {
  if (!req.session.cart) req.session.cart = [];
  const cartWithDetails = await Promise.all(req.session.cart.map(async item => {
    const product = await db.collection('Products').findOne({ _id: new ObjectId(item.productId) });
    return { product, quantity: item.quantity };
  }));
  res.json({ cart: cartWithDetails });
});

// API xóa sản phẩm khỏi giỏ hàng
app.delete('/api/cart/remove', (req, res) => {
  const { productId } = req.body;
  req.session.cart = req.session.cart.filter(item => item.productId !== productId);
  res.send('Product removed from cart');
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
