import logging
import csv

# Cấu hình logging (tốt hơn print cho dự án thực tế)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",  # Lưu log ra file
)


def process_csv(filepath):
    logging.info(f"Bắt đầu xử lý file: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                logging.debug(f"Hàng {i}: {row}")
    except Exception as e:
        logging.error(f"Lỗi: {e}", exc_info=True)


process_csv("data.csv")
