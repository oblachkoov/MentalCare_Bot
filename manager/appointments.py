from datetime import datetime
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from model.appointments import Appointment


class AppointmentManager:
    def __init__(self, db: AsyncSession):
        self.db = db



    async def create(self, client_id: int):
        stmt = (
            insert(Appointment)
            .values(
                client_id=client_id,
                status="pending",
                created_at=datetime.utcnow()
            )
            .returning(Appointment)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()


    async def get_client_appointments(self, client_id: int):
        stmt = select(Appointment).where(Appointment.client_id == client_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()


    async def get_new_requests(self):
        stmt = select(Appointment).where(Appointment.status == "pending")
        result = await self.db.execute(stmt)
        return result.scalars().all()


    async def take_client(self, appointment_id: int, psychologist_id: int):
        stmt = (
            update(Appointment)
            .where(
                Appointment.id == appointment_id,
                Appointment.status == "pending"
            )
            .values(
                psychologist_id=psychologist_id,
                status="in_progress"
            )
        )
        await self.db.execute(stmt)
        await self.db.commit()



    async def get_my_clients(self, psychologist_id: int):
        stmt = (
            select(Appointment)
            .where(
                Appointment.psychologist_id == psychologist_id,
                Appointment.status == "in_progress"
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()



    async def mark_done(self, appointment_id: int, psychologist_id: int):
        stmt = (
            update(Appointment)
            .where(
                Appointment.id == appointment_id,
                Appointment.psychologist_id == psychologist_id,
                Appointment.status == "in_progress"
            )
            .values(
                status="done",
                finished_at=datetime.utcnow()
            )
        )
        await self.db.execute(stmt)
        await self.db.commit()



    async def get_history_appointments(self, psychologist_id: int):
        stmt = (
            select(Appointment)
            .where(
                Appointment.psychologist_id == psychologist_id,
                Appointment.status == "done"
            )
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()
