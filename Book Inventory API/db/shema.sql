CREATE TABLE authors (
    author_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

CREATE TABLE books (
    book_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id BIGINT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_author
        FOREIGN KEY (author_id) 
        REFERENCES authors (author_id)
        ON DELETE CASCADE
);

CREATE INDEX idx_books_author_id ON books (author_id);
