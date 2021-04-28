class BlogRouter:
    """
    A router to control all database operations on models in the
    blog application.
    """
    route_app_labels = {'blog'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read blog models go to the 'blog' db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'blog'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write blog models go to 'blog' db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'blog'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in blog is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the blog app only appears in the
        'blog' database.
        """
        if app_label in self.route_app_labels:
            return db == 'blog'
        return None