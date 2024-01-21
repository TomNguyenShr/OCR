def iden(ocr,file):
    wordlist = ocr.split("\n")
    result = [file,"N/A", "N/A", "N/A", "N/A"]
    for word in wordlist:
        if "khach hang:" in word.lower():
            new = word.lower().replace("khach hang:", "")
            result[1] = new
        if "thu ngan:" in word.lower():
            new = word.lower().replace("thu ngan:", "")
            result[2] = new
        if "tong so:" in word.lower():
            new = word.lower().replace("tong so:", "")
            result[3] = new
        if "ngay" in word.lower():
            new = word.lower().replace("ngay", "")
            result[4] = new
    return result
