from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update
from model.notes import Note
from typing import List, Optional

class NoteManager:
    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self, user_id: int, text: Optional[str] = None, file_url: Optional[str] = None) -> Note:
        note = Note(user_id=user_id, text=text, file_url=file_url)
        self.db.add(note)
        await self.db.commit()
        await self.db.refresh(note)
        return note


    async def get_user_notes(self, user_id: int) -> List[Note]:
        result = await self.db.execute(select(Note).where(Note.user_id == user_id).order_by(Note.created_at.desc()))
        return result.scalars().all()


    async def get_by_id(self, note_id: int) -> Optional[Note]:
        result = await self.db.execute(select(Note).where(Note.id == note_id))
        return result.scalars().first()




    async def delete(self, note_id: int) -> bool:
        note = await self.get_by_id(note_id)
        if not note:
            return False
        await self.db.delete(note)
        await self.db.commit()
        return True
