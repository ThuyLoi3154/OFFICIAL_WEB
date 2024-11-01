import base64
import pymongo

# Kết nối tới MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["products_database"]       # Tên database của bạn
collection = db["MILK"]           # Tên collection của bạn

# Hàm chuyển đổi một danh sách hình ảnh thành mảng base64
def encode_images(image_files):
    encoded_images = []
    for file in image_files:
        with open(file, "rb") as image_file:
            encoded_images.append(base64.b64encode(image_file.read()).decode('utf-8'))
    return encoded_images

# Chuẩn bị danh sách sản phẩm
products = [
    {
        "name": "Sữa đậu phộng nguyên vị",
        "category": "MILK",
        "price": 25000,
        "description": "Thành phần: Nước, đậu phộng, mật mía, muối. Bảo quản: trong tủ lạnh 1-5 độ C. Cảnh báo: Không sử dụng cho người dị ứng với các thành phần của sản phẩm. Có thể có dấu vết của điều. NSX: Xem trên bao bì. HSD: Trong ngày.",
        "images": encode_images()
    },
    {
        "name": "Sữa đậu phộng cải kale",
        "category": "MILK",
        "price": 32000,
        "description": "Thành phần: Nước, đậu phộng, mật mía, bột cải kale, muối. Bảo quản: trong tủ lạnh 1-5 độ C. Cảnh báo: Không sử dụng cho người dị ứng với các thành phần của sản phẩm. Có thể có dấu vết của điều. NSX: Xem trên bao bì. HSD: Trong ngày.",
        "images": encode_images()
    },
    {
        "name": "Sữa gạo diêm mạch",
        "category": "MILK",
        "price": 199000,
        "description": "Chứng nhận hữu cơ: Được chứng nhận hữu cơ IT-BIO-007 Agricoltura/non UE. Không chứa Gluten: Sản phẩm hoàn toàn an toàn cho những người nhạy cảm với gluten. Ít béo: Cung cấp sự lựa chọn lành mạnh cho chế độ ăn uống hàng ngày. Không thêm đường: Hoàn toàn tự nhiên, không chứa đường tinh luyện. Không chứa Lactose: Phù hợp cho người ăn kiêng lactose và người bị dị ứng.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt điều cacao",
        "category": "MILK",
        "price": 32000,
        "description": "Thành phần: Nước, hạt điều, mật mía, bột cacao, muối. Bảo quản: trong tủ lạnh 1-5 độ C. Cảnh báo: Không sử dụng cho người dị ứng với các thành phần của sản phẩm. Có thể có dấu vết của đậu phộng. NSX: Xem trên bao bì. HSD: Trong ngày.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt điều củ dền",
        "category": "MILK",
        "price": 32000,
        "description": "Thành phần: Nước, đậu phộng, mật mía, muối.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt điều nguyên vị",
        "category": "MILK",
        "price": 27000,
        "description": "Thành phần: Nước, hạt điều, mật mía, muối. Bảo quản: trong tủ lạnh 1-5 độ C. Cảnh báo: Không sử dụng cho người dị ứng với các thành phần của sản phẩm. Có thể có dấu vết của đậu phộng. NSX: Xem trên bao bì. HSD: Trong ngày.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt hạnh nhân 1L",
        "category": "MILK",
        "price": 220000,
        "description": "✓ Vị Sữa Béo và Thơm Ngon Được Người Úc Yêu Thích: Với công thức độc quyền, Sữa Hạnh Nhân Barista’s Choice FIT&FRESH mang đến vị sữa béo ngậy, thơm ngon, chinh phục mọi tín đồ yêu thích đồ uống từ sữa. ✓ Hương Vị Đậm Đà, Cân Bằng & Mịn Màng, Dễ Uống: Sản phẩm có hương vị đậm đà và cân bằng hoàn hảo, giúp tách biệt hương cà phê và sữa, tạo nên một ly cà phê thơm ngon, hấp dẫn. Độ sánh mịn vừa phải, không quá loãng cũng không quá đặc, tạo nên lớp bọt sữa mềm mịn đẹp mắt trên những ly latte, cappuccino. ✓ Giàu Canxi: Với hàm lượng canxi cao (mỗi ly 250ml cung cấp 36% nhu cầu canxi hàng ngày), Sữa Hạt FIT&FRESH hỗ trợ xương chắc khỏe, giúp phát triển chiều cao ở trẻ em và ngăn ngừa loãng xương ở người lớn tuổi.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt ngũ cốc không đường",
        "category": "MILK",
        "price": 22000,
        "description": "Các thành phần chính: Mầm gạo lứt hoa nhài, Mầm lúa mì, Yến mạch. Giới thiệu sản phẩm: Sữa ngũ cốc FIT&FRESH là một lựa chọn bổ dưỡng và tự nhiên, cung cấp nhiều lợi ích cho sức khỏe. Gạo lứt được thu được từ hạt lúa xay xát lần đầu, giữ lại mầm và cám gạo, giúp sản phẩm giàu protein, vitamin, chất xơ và nguyên tố vi lượng. Khác với gạo trắng, sau khi đã qua nhiều lần xay xát, mầm và cám gạo không còn tồn tại. Mầm lúa mì và yến mạch là hai thành phần giàu dinh dưỡng, cung cấp nhiều hoạt chất chống oxi hóa, vitamin E và vitamin B, hỗ trợ tiêu hóa, và ngăn chặn hấp thu cholesterol hiệu quả. Lợi ích của Gamma-Oryzanol: Sữa ngũ cốc FIT&FRESH còn chứa Gamma-Oryzanol, một hoạt chất tự nhiên với đặc tính chống oxi hóa mạnh, giúp ức chế sự hình thành các tế bào gốc tự do, giảm nguy cơ mắc bệnh lão hóa và ung thư. Nghiên cứu cho thấy gamma-oryzanol có khả năng giảm lượng cholesterol LDL (cholesterol xấu) trong máu, hỗ trợ cân bằng hormone, giảm triệu chứng khó chịu trong giai đoạn mãn kinh và giữ ẩm cho da.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt ngũ cốc mè đen",
        "category": "MILK",
        "price": 22000,
        "description": "Các thành phần chính: Mầm gạo lứt hoa nhài, Mầm lúa mì, Yến mạch. Giới thiệu sản phẩm: Sữa ngũ cốc FIT&FRESH là sự kết hợp hoàn hảo giữa các thành phần tự nhiên, mang lại nhiều lợi ích cho sức khỏe. Gạo lứt, thu được từ hạt lúa xay xát lần đầu, giữ lại mầm và cám gạo, cung cấp một nguồn dinh dưỡng dồi dào với protein, vitamin, chất xơ và các nguyên tố vi lượng. Khác với gạo trắng đã qua nhiều lần xay xát, gạo lứt vẫn giữ được các chất dinh dưỡng quý giá này.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt ngũ cốc socola",
        "category": "MILK",
        "price": 22000,
        "description": "Thành phần: Nước mầm gạo lứt hoa nhài (35%), Nước mầm lúa mì (28%), Nước yến mạch (25.5%), Đường mía (4%), Chất xơ (2.4%), Sô cô la (2%),..",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt ngũ cốc truyền thống",
        "category": "MILK",
        "price": 22000,
        "description": "Thành phần chính: Mầm gạo lứt hoa nhài, Mầm lúa mì, Yến mạch. Sữa ngũ cốc FIT&FRESH còn chứa Gamma-Oryzanol, một hoạt chất chống oxi hóa mạnh, có tác dụng ức chế sự hình thành tế bào gốc tự do và giúp giảm cholesterol LDL (cholesterol xấu) trong máu.",
        "images": encode_images()
    },
    {
        "name": "Sữa tươi hữu cơ vị chuối",
        "category": "MILK",
        "price": 42000,
        "description": "Sữa tươi hữu cơ FIT&FRESH là dòng sữa tách béo, chứa ít đường và chỉ sử dụng màu sắc cùng hương vị tự nhiên, không có các chất phụ gia nhân tạo hay chất bảo quản. Thành phần của sữa hoàn toàn tuân thủ các quy định dinh dưỡng dành cho học sinh tại Việt Nam. Cụ thể, sữa chứa hàm lượng đường ít hơn 5%.",
        "images": encode_images()
    },
    {
        "name": "Sữa yến mạch hữu cơ",
        "category": "MILK",
        "price": 199000,
        "description": "Sữa Yến Mạch Canxi Hữu Cơ FIT&FRESH là lựa chọn lý tưởng cho những ai tìm kiếm sản phẩm dinh dưỡng lành mạnh và tự nhiên. Được làm từ yến mạch hữu cơ chất lượng cao, sản phẩm không chỉ mang đến hương vị thơm ngon mà còn cung cấp nguồn canxi dồi dào, hỗ trợ sức khỏe xương và răng.",
        "images": encode_images()
    },
    {
        "name": "Sữa yến mạch không đường 1L",
        "category": "MILK",
        "price": 230000,
        "description": "Sữa yến mạch FIT&FRESH đang nổi lên như một sản phẩm “hot trend” trong giới pha chế, đặc biệt trong các thức uống matcha latte, và hiện là sự lựa chọn được ưa chuộng nhất.Được thiết kế đặc biệt để mang đến sự kết hợp hoàn hảo giữa độ béo ngọt vừa phải và kết cấu mịn màng, không quá ngấy hay quá ngọt. Đây là lựa chọn lý tưởng cho các barista và những ai yêu thích pha chế đồ uống.",
        "images": encode_images()
    },
    {
        "name": "Sữa yến mạch mix coffee 1L",
        "category": "MILK",
        "price": 230000,
        "description": "SỮA YẾN MẠCH MIX COFFEE 1L Được chứng nhận hữu cơ IT-BIO-007 Agricoltura/non UE. THÀNH PHẦN: Nước, yến mạch (16%), dầu gạo, chất ổn định: natri polyphosphate, muối. Hạn sử dụng: Trong 12 tháng kể từ ngày sản xuất CÁCH SỬ DỤNG: Hoàn hảo để tạo bọt vào cà phê của bạn để có một ly cà phê cappuccino Ý đích thực!",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt cao đạm ít đường",
        "category": "MILK",
        "price": 25000,
        "description": "Chứa “đạm hoàn chỉnh”, cung cấp đủ 9 loại amino acids thiết yếu mà cơ thể không tự tổng hợp được: histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan và valine – hỗ trợ miễn dịch, hấp thu dinh dưỡng và sản xuất năng lượng.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt đậu nành đậu đỏ ít đường",
        "category": "MILK",
        "price": 25000,
        "description": "Sự kết hợp nhuần nhuyễn của đậu nành chín tới cùng những hạt óc chó tròn mẩy, đậu đỏ mới tách hạt, hạnh nhân vào mùa tạo nên tuyển tập hương vị phong phú của sữa đậu nành FIT&FRESH.VN. ",
        "images": encode_images()
    },
    {
        "name": "Sữa tươi nguyên chất không đường",
        "category": "MILK",
        "price": 25000,
        "description": "Đầu bếp Top 1% thế giới chấm điểm cao tuyệt đối về vị ngon. Chinh phục giải thưởng có giám khảo top đầu bếp thế giới và đạt chứng nhận an toàn tinh khiết khắt khe từ Mỹ. Công nghệ kép đột phá: Hút chân không sữa giảm đến 50% gốc oxy tự do, khoá tươi tức thời, loại bỏ các tạp vị, lưu giữ tối đa hương cỏ hoa và vị thơm tự nhiên của sữa.",
        "images": encode_images()
    },
    {
        "name": "Sữa hạt đậu nành óc chó ít đường",
        "category": "MILK",
        "price": 25000,
        "description": "Có hương vị béo bùi đặc trưng, đến từ dưỡng chất nổi trội nhất: chất béo tốt – chiếm 65% trọng lượng hạt, phần lớn là ALA (Omega-3) và Omega-6, giúp giảm huyết áp, giảm cholesterol xấu, hỗ trợ sức khỏe não bộ và tim mạch. ​",
        "images": encode_images()
    },
    {
        "name": "Sữa tươi nguyên chất ít đường",
        "category": "MILK",
        "price": 25000,
        "description": "Đầu bếp Top 1% thế giới chấm điểm cao tuyệt đối về vị ngon Chinh phục giải thưởng có giám khảo top đầu bếp thế giới và đạt chứng nhận an toàn tinh khiết khắt khe từ Mỹ. Công nghệ kép đột phá: Hút chân không sữa giảm đến 50% gốc oxy tự do, khoá tươi tức thời, loại bỏ các tạp vị, lưu giữ tối đa hương cỏ hoa và vị thơm tự nhiên của sữa.",
        "images": encode_images()
    },
]

# Lưu tất cả sản phẩm vào MongoDB cùng lúc
collection.insert_many(products)
print("Tất cả sản phẩm đã được lưu vào MongoDB.")
