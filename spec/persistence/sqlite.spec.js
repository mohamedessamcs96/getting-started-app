const db = require('../../src/persistence/sqlite'); // Adjust path as necessary

const ITEM = { id: '1', name: 'Test Item', completed: false };

beforeEach(async () => {
    await db.init();
    // Clear the database before each test
    await new Promise((resolve, reject) => {
        db.db.run('DELETE FROM todo_items', (err) => {
            if (err) reject(err);
            else resolve();
        });
    });
});

afterEach(async () => {
    await db.teardown();
});

describe('sqlite persistence', () => {
    test('it can update an existing item', async () => {
        const initialItems = await db.getItems();
        expect(initialItems.length).toBe(0); // Ensure no items initially

        await db.storeItem(ITEM);

        const itemsAfterStore = await db.getItems();
        expect(itemsAfterStore.length).toBe(1); // Item should be stored

        await db.updateItem(ITEM.id, { name: 'Updated Item', completed: true });

        const updatedItem = await db.getItem(ITEM.id);
        expect(updatedItem.name).toBe('Updated Item');
        expect(updatedItem.completed).toBe(true); // Item should be updated
    });
});
