CREATE TABLE members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    signup_date DATE,
    birth_year INT,
    gender VARCHAR(10),
    marketing_agree BOOLEAN,
    last_login_at DATETIME,
    member_type VARCHAR(20)
);

CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    instructor_name VARCHAR(50),
    bio TEXT,
    profile_image VARCHAR(255)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_code VARCHAR(20),
    category_name VARCHAR(50),
    parent_category VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_code VARCHAR(20),
    course_title VARCHAR(200),
    category_id INT,
    instructor_id INT,
    price INT,
    sale_price INT,
    course_level VARCHAR(20),
    total_minutes INT,
    published_date DATE,
    course_status VARCHAR(20),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

CREATE TABLE sections (
    section_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    section_no INT,
    section_title VARCHAR(200),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE lessons (
    lesson_id INT PRIMARY KEY AUTO_INCREMENT,
    section_id INT,
    lesson_no INT,
    lesson_title VARCHAR(200),
    lesson_minutes INT,
    is_free BOOLEAN,
    FOREIGN KEY (section_id) REFERENCES sections(section_id)
);

CREATE TABLE tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(50) UNIQUE
);

CREATE TABLE course_tags (
    course_id INT,
    tag_id INT,
    PRIMARY KEY (course_id, tag_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    course_id INT,
    enrolled_at DATETIME,
    progress_rate DECIMAL(5,2),
    last_lesson_id INT,
    is_completed BOOLEAN,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (last_lesson_id) REFERENCES lessons(lesson_id)
);

CREATE TABLE payment_methods (
    payment_method_id INT PRIMARY KEY AUTO_INCREMENT,
    method_name VARCHAR(30)
);

CREATE TABLE coupons (
    coupon_id INT PRIMARY KEY AUTO_INCREMENT,
    coupon_code VARCHAR(50) UNIQUE,
    discount_type VARCHAR(20),
    discount_value INT
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    payment_method_id INT,
    coupon_id INT,
    original_price INT,
    discount_amount INT,
    payment_amount INT,
    paid_at DATETIME,
    refunded_at DATETIME,
    refund_amount INT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id),
    FOREIGN KEY (coupon_id) REFERENCES coupons(coupon_id)
);

CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    course_id INT,
    lesson_id INT,
    created_at DATETIME,
    rating INT,
    review_title VARCHAR(200),
    review_content TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
);

CREATE TABLE inquiries (
    inquiry_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    course_id INT NULL,
    lesson_id INT NULL,
    created_at DATETIME,
    inquiry_title VARCHAR(200),
    inquiry_content TEXT,
    answered_at DATETIME,
    answered_by INT NULL,
    inquiry_status VARCHAR(20),
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
    FOREIGN KEY (answered_by) REFERENCES members(member_id)
);