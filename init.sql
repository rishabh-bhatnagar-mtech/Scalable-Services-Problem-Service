CREATE TABLE IF NOT EXISTS problems
(
    id           SERIAL PRIMARY KEY,
    title        VARCHAR(255) NOT NULL,
    difficulty   VARCHAR(20) CHECK (difficulty IN ('easy', 'medium', 'hard')),
    description  TEXT         NOT NULL,
    starter_code JSONB        NOT NULL,
    test_cases   JSONB        NOT NULL,
    constraints  TEXT[]      DEFAULT ARRAY []::TEXT[],
    created_at   TIMESTAMPTZ DEFAULT NOW(),
    updated_at   TIMESTAMPTZ DEFAULT NOW()
);
