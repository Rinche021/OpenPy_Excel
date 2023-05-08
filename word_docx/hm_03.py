from docx import Document

# Создаем новый документ
document = Document()

# Добавляем текст в документ
document.add_paragraph("Hello Python")

# Сохраняем документ
document.save("document.docx")

# Возникли проблемы с пакетом
