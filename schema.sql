DROP TABLE IF EXISTS posts;

CREATE TABLE defects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    number INTEGER NOT NULL,
    equipment TEXT NOT NULL,
    description TEXT NOT NULL,
    user_start TEXT NOT NULL,
    time_finish TIMESTAMP,
    fix_descr TEXT,
    repairman TEXT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fixed TIMESTAMP
);