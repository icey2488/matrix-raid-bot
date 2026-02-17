from .base import command, CommandContext

@command("signup")
async def signup_cmd(ctx: CommandContext):
    await ctx.services.matrix.send_text(ctx.room_id, "Signup command placeholder.")