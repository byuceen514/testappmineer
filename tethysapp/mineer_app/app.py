from tethys_sdk.base import TethysAppBase, url_map_maker


class TestAppForSam(TethysAppBase):
    """
    Tethys app class for Test App for Sam.
    """

    name = 'Test App for Sam'
    index = 'mineer_app:home'
    icon = 'mineer_app/images/icon.gif'
    package = 'mineer_app'
    root_url = 'mineer-app'
    color = '#2ecc71'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='mineer-app',
                           controller='mineer_app.controllers.home'),
        )

        return url_maps