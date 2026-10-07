# SKU generator

from pyscript import document


def generate_sku(category, product_name, stock_qty):

    cat_code = category.strip().upper()[:3].ljust(3, "X")

    clean_name = "".join(filter(str.isalpha, product_name)).upper()
    name_code = clean_name[:3].ljust(3, "X")

    qty_code = str(stock_qty).zfill(2)[:2]

    sku_code = f"{cat_code}{name_code}{qty_code}"

    return sku_code


def generate_sku_from_html(event):

    category = document.getElementById("category").value
    product_name = document.getElementById("productName").value
    stock_qty = document.getElementById("stockQty").value

    if product_name.strip() == "" or stock_qty == "":
        document.getElementById("skuOutput").style.display = "block"
        document.getElementById("skuResult").innerHTML = "Please enter all information."
        return

    sku_code = generate_sku(category, product_name, stock_qty)

    cat_code = category.strip().upper()[:3].ljust(3, "X")

    clean_name = "".join(filter(str.isalpha, product_name)).upper()
    name_code = clean_name[:3].ljust(3, "X")

    qty_code = str(stock_qty).zfill(2)[:2]

    document.getElementById("skuResult").innerHTML = sku_code
    document.getElementById("skuCatCode").innerHTML = cat_code
    document.getElementById("skuItemCode").innerHTML = name_code
    document.getElementById("skuQtyCode").innerHTML = qty_code

    document.getElementById("skuOutput").style.display = "block"