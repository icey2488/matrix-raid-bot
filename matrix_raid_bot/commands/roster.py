from .base import command, CommandContext

@command("roster")
async def roster_cmd(ctx: CommandContext):
    await ctx.services.matrix.send_text(ctx.room_id, "Roster command placeholder.")