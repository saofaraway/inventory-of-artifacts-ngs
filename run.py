from app import create_app
from app.extensions import db
from app.models import User
from app.extensions import bcrypt

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Clear the existing data and create new tables with a default admin."""
    db.create_all()
    
    # Create default Admin
    if not User.query.filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@artefak.com',
            password_hash=bcrypt.generate_password_hash('admin123').decode('utf-8'),
            role='Admin'
        )
        db.session.add(admin)
        
    # Create default Staff Koleksi
    if not User.query.filter_by(username='koleksi').first():
        koleksi = User(
            username='koleksi',
            email='koleksi@artefak.com',
            password_hash=bcrypt.generate_password_hash('koleksi123').decode('utf-8'),
            role='Staff Koleksi'
        )
        db.session.add(koleksi)
        
    # Create default Staff Konservasi
    if not User.query.filter_by(username='konservasi').first():
        konservasi = User(
            username='konservasi',
            email='konservasi@artefak.com',
            password_hash=bcrypt.generate_password_hash('konservasi123').decode('utf-8'),
            role='Staff Konservasi'
        )
        db.session.add(konservasi)

    # Create default Staff Perpindahan
    if not User.query.filter_by(username='pindah').first():
        pindah = User(
            username='pindah',
            email='pindah@artefak.com',
            password_hash=bcrypt.generate_password_hash('pindah123').decode('utf-8'),
            role='Staff Perpindahan'
        )
        db.session.add(pindah)

    db.session.commit()
    print("Database initialized and default users created.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
