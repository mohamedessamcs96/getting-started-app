const db = require('../../src/persistence/sqlite');
const path = require('path');
const fs = require('fs');

const ITEM = { id: '1', name: 'Test Item', completed: false };

beforeEach(async () => {
    // Use a test-specific database file
    process.env.SQLITE_DB_LOCATION = path.join(__dirname, 'test-todo.db');
    
    // Clean up the test database file before each test
    if (fs.existsSync(process.env.SQLITE_DB_LOCATION)) {
        fs.unlinkSync(process.env.SQLITE_DB_LOCATION);
    }

    await db.init();
});

afterEach(async () => {
    await db.teardown();
    // Clean up the test database file after each test
    if (fs.existsSync(process.env.SQLITE_DB_LOCATION)) {
        fs.unlinkSync(process.env.SQLITE_DB_LOCATION);
    }
});
