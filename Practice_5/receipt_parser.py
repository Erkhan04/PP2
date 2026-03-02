import re
import json
from typing import List, Dict, Any

def to_number(s: str) -> float:
    """
    Convert numbers like:
    '1 200,00' -> 1200.00
    '18 009,00' -> 18009.00
    '2,000' -> 2.0
    """
    s = s.replace("\u00A0", " ")         
    s = s.replace(" ", "")               
    s = s.replace(",", ".")             
    return float(s)

def parse_receipt(text: str) -> Dict[str, Any]:
    # 1) Items block regex
    item_pattern = re.compile(
        r"(?m)^\s*(?P<idx>\d+)\.\s*\n"                   
        r"(?P<name>.*?)\n"                                  
        r"(?P<qty>\d+,\d+)\s*x\s*(?P<unit>\d[\d ]*,\d{2})\n" 
        r"(?P<line>\d[\d ]*,\d{2})",                        
        re.DOTALL
    )

    items: List[Dict[str, Any]] = []
    for m in item_pattern.finditer(text):
        name = m.group("name").strip()
        name = re.sub(r"\s*\n\s*", " ", name)

        qty = to_number(m.group("qty"))
        unit_price = to_number(m.group("unit"))
        line_total = to_number(m.group("line"))

        items.append({
            "index": int(m.group("idx")),
            "name": name,
            "quantity": qty,
            "unit_price": unit_price,
            "line_total": line_total
        })

    # 2) Total from "ИТОГО:"
    total_match = re.search(r"(?m)^\s*ИТОГО:\s*\n\s*(\d[\d ]*,\d{2})\s*$", text)
    total = to_number(total_match.group(1)) if total_match else None

    # 3) Payment method + amount, like:
    pay_match = re.search(r"(?m)^\s*(Банковская карта|Наличные|Kaspi|Карта|Card)\s*:\s*\n\s*(\d[\d ]*,\d{2})", text)
    payment_method = pay_match.group(1) if pay_match else None
    payment_amount = to_number(pay_match.group(2)) if pay_match else None

    # 4) Date & time from:
    dt_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
    date = dt_match.group(1) if dt_match else None
    time = dt_match.group(2) if dt_match else None

    # 5) Optional: branch / company (шапка)
    company_match = re.search(r"(?m)^\s*Филиал\s+(.+)$", text)
    company = company_match.group(0).strip() if company_match else None

    # 6) Calculated total from lines (на всякий случай)
    calculated_total = round(sum(i["line_total"] for i in items), 2)

    return {
        "company_line": company,
        "date": date,
        "time": time,
        "payment_method": payment_method,
        "payment_amount": payment_amount,
        "items": items,
        "total": total,
        "calculated_total": calculated_total,
        "items_count": len(items)
    }

if __name__ == "__main__":
    with open("raw.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    data = parse_receipt(raw)
    print(json.dumps(data, ensure_ascii=False, indent=2))