import random2 

# List of Thai first names
first_names = ['กมล', 'จิรายุ', 'ธนพล', 'ณัฐชา', 'ประภา', 'พรชัย', 'มนต์ชัย', 'ยุพิน', 'รัชนู', 'วิชัย', 'สุชาติ', 'อรุณ']

# List of Thai last names
last_names = ['กิติศักดิ์', 'จันทร์เจริญ', 'ธีระวัฒน์', 'ณ วิชัย', 'ประเสริฐ', 'พงศ์พันธุ์', 'มงคล', 'ยงยุทธ', 'รัตนโกสินทร์', 'วงศ์สว่าง', 'สุขสันต์', 'อัครพงศ์']

# List of Thai provinces
provinces = ['กรุงเทพมหานคร', 'เชียงใหม่', 'ขอนแก่น', 'นครราชสีมา', 'ภูเก็ต', 'สมุทรปราการ', 'นนทบุรี', 'ปทุมธานี', 'นครศรีธรรมราช', 'เชียงราย', 'นครสวรรค์', 'สุราษฎร์ธานี']

# Generate a random Thai name
first_name = random2.choice(first_names)
last_name = random2.choice(last_names)
full_name = f'{first_name} {last_name}'

# Generate a random Thai address
province = random2.choice(provinces)
district = f'เขต{random2.randint(1, 50)}'
sub_district = f'แขวง{random2.choice(["สามวาตะวันตก", "สามวาตะวันออก", "บางชัน", "บางนา", "บางเมือง"])}'
address = f'{random2.randint(1, 999)} {sub_district} {district} {province} {random2.randint(10000, 99999)}'

# Generate a random Thai phone number
phone_number = f'0{random2.choice(["6", "8", "9"])}{random2.randint(10000000, 99999999)}'

# Print the generated Thai name, address, and phone number
print(f'Name: {full_name}')
print(f'Address: {address}')
print(f'Phone Number: {phone_number}')
