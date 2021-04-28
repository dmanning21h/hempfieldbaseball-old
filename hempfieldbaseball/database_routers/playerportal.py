class PlayerportalRouter:
    """
    A router to control all database operations on models in the
    playerportal application.
    """
    route_app_labels = {
        'playerportal', 'admin', 'auth', 'contenttypes', 'sessions'
    }

    def db_for_read(self, model, **hints):
        """
        Attempts to read playerportal models go to the 'playerportal' db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'playerportal'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write playerprotal models go to 'playerportal' db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'playerportal'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in playerportal is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the playerportal app only appears in the
        'playerportal' database.
        """
        if app_label in self.route_app_labels:
            return db == 'playerportal'
        return None