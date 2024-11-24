Your code looks well-structured and should generate meaningful and unique IDs for the `MembershipType`, `Member`, and `Attendance` models. Here's a quick summary of how the ID generation works for each model:

### 1. **`MembershipType` Model**:
   - The `membership_type_id` is generated in the format `MT-{duration}-{cost}`, where:
     - `duration` is zero-padded to 3 digits.
     - `cost` is zero-padded to 4 digits.
   - Example: A membership with a duration of 12 months and a cost of 1500 INR will have an ID like `MT-012-1500`.

### 2. **`Member` Model**:
   - The `member_id` is generated using:
     - The first three characters of the `last_name` (uppercase).
     - The `year_of_joining` (extracted from `date_of_joining`).
     - A sequential number (starting from 001) for members who joined in the same year.
   - Example: The first member of the year 2023 with the last name starting with "Smith" would have an ID like `SMT-2023-001`.

### 3. **`Attendance` Model**:
   - The `attendance_id` is generated using:
     - The `member_id` of the member.
     - The `date` of the attendance (formatted as `YYYYMMDD`).
     - A sequential number for each attendance on the same day (starting from 01).
   - Example: The first attendance of the member `SMT-2023-001` on November 24, 2023, will have an ID like `SMT-2023-001-20231124-01`.

### Additional Notes:
- The **`save()`** method in each model ensures that these IDs are automatically generated when the object is saved to the database, so you don't have to manually set the ID each time you create a new object.
- The IDs are based on logical and meaningful components, making them easy to understand and traceable.





### 1. **MembershipType POST Request**
**Endpoint**: `/membership-types/`  
**Sample JSON**:
```json
{
    "membership_type_id": "MT-012-1000",
    "duration": 12,
    "cost": 1000.00
}
```



### 2. **Member POST Request**
**Endpoint**: `/members/`  
**Sample JSON**:
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_joining": "2024-11-24",
    "email": "johndoe@example.com",
    "address": "123 Main Street, City, Country",
    "phone": "+1234567890",
    "membership_type": "MT-012-1000"
}
```

---

### 3. **Attendance POST Request**
**Endpoint**: `/attendance/`  
**Sample JSON**:
```json
{
    "member": "DOE-2024-001",
    "date": "2024-11-24",
    "check_in_time": "09:00:00",
    "check_out_time": "17:00:00"
}
```

---

### Notes:
1. **`membership_type_id`** in `MembershipType` should match the primary key or ID format expected.
2. **`membership_type`** in `Member` should be a valid `membership_type_id` from the `MembershipType` table.
3. **`member`** in `Attendance` should be a valid `member_id` from the `Member` table.
4. Ensure the `date_of_joining` and `date` fields follow the `YYYY-MM-DD` format.
5. Time fields like `check_in_time` and `check_out_time` must follow the `HH:MM:SS` format.
