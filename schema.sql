CREATE TABLE IF NOT EXISTS builds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    build_number INT,
    status VARCHAR(30),
    duration_sec INT,
    timestamp BIGINT,
    job_name VARCHAR(100)
);
