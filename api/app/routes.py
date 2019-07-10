from app.models import StreamLog, User
from flask import request, make_response
from app import app
from app import db
import sqlalchemy
@app.route("/<email>/logs",methods=['GET'])
def list_logs_for_user(email):
    u=db.session.query(User).filter_by(email=email).first()
    res="#ip;content_id;date<br>"
    res+="<br>".join(["{};<a href='https://www.youtube.com/watch?v={}'>{}</a>;{}".format(p.ip,p.content_id,p.content_id,p.timestamp) for p in u.posts])
    return make_response(res, 200)

@app.route("/",methods=['GET'])
def list_users():
    out="\n".join(["<a href='"+u.email+"/logs' > "+u.email+"</a><br>" for u in db.session.query(User).all()])
    return make_response(out, 200)



@app.route("/<email>",methods=['POST'])
def create_user(email):
    u=User(email=email)
    db.session.add(u)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return make_response("This email already exists", 409)

    return make_response("CREATED", 201)



@app.route("/<email>/<content_id>",methods=['POST'])
def add_log_for_user(email,content_id):
    u=db.session.query(User).filter_by(email=email).first()
    if u is None:
        return make_response("NO SUCH EMAIL REGISTERED", 404)
    s=StreamLog(content_id=content_id,ip=request.remote_addr,user=u)
    db.session.add(s)
    db.session.commit()
    return make_response("CREATED {} {}".format(s.content_id,u.email), 201)

