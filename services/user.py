from datetime import datetime
from sqlalchemy import select, update
from models.user import User


class UserService:
    def __init__(self, session):
        self.session = session

    async def get_by_tg_id(self, telegram_id: int):
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def update_last_activity(self, telegram_id: int):
        stmt = update(User).where(User.telegram_id == telegram_id).values(
            last_activity=datetime.now()
        )
        await self.session.execute(stmt)
        await self.session.commit()



