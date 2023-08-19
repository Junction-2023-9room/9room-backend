from fastapi import APIRouter, HTTPException

router = APIRouter()

companies_data = {
    "jaka": {
        "name": "Jaka",
        "nameImg": "/images/company/jaka-logo.svg",
        "img": "/images/company/jaka-img.png",
        "location": "Near Seoul",
        "time": "Within 2 days",
        "rating": "4.5",
        "desc": "Impressed with their use of cobot. The disposal process was not only efficient.",
        "cheaper": "30%",
        "reviewCount": 10,
        "price": 100000,
        "images": ["/images/company/jaka-1.png", "/images/company/jaka-2.png"],
    },
    "jaka2": {
        "name": "Jaka2",
        "nameImg": "/images/company/jaka-logo.svg",
        "img": "/images/company/jaka-img.png",
        "location": "Near Seoul",
        "time": "Within 2 days",
        "rating": "4.5",
        "desc": "Impressed with their use of cobot. The disposal process was not only efficient.",
        "cheaper": "30%",
        "reviewCount": 10,
        "price": 100000,
        "images": ["/images/company/jaka-1.png", "/images/company/jaka-2.png"],
    },
}

@router.get("/companies/")
def get_companies():
    return companies_data

# If you want to get a specific company's details by their name, you can also add the following:

@router.get("/companies/{company_name}")
def get_company(company_name: str):
    company = companies_data.get(company_name)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
