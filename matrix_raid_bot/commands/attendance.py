from .base import command, CommandContext

@command("attendance")
async def attendance_cmd(ctx: CommandContext):
    await ctx.services.matrix.send_text(ctx.room_id, "Attendance command placeholder.")