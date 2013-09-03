from jinja2 import evalcontextfilter, Markup

@evalcontextfilter
def video_embed(eval_ctx, post_obj, size=400):
    if size not in [250, 400, 500, 700]:
        size = 700
    result = ''
    for player_obj in post_obj.get('player'):
        if player_obj.get('width') == size:
            result = player_obj.get('embed_code')
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
