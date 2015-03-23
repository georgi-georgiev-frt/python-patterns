#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://en.wikipedia.org/wiki/Factory_method_pattern
The good point over the SimpleFactory is you can subclass it to implement different ways to create objects
For simple case, this abstract class could be just an interface
This pattern is a "real" Design Pattern because it achieves the "Dependency Inversion Principle"
a.k.a the "D" in S.O.L.I.D principles.
"""

from abc import ABCMeta, abstractmethod  # Be able writing abstract classes


# Factories

class VideoFactory:  # This is an interface to keep it simple
    VIDEO_TYPE_COMMERCIAL = 'commercial'
    VIDEO_TYPE_TUTORIAL = 'tutorial'

    def __init__(self):
        pass

    def create_video(self, video_type, video_src):
        raise NotImplementedError


class SiteOneVideoFactory(VideoFactory):
    """
    This site hosts its videos on Youtube
    """

    def create_video(self, video_type, video_id):
        if video_type == VideoFactory.VIDEO_TYPE_COMMERCIAL:
            return YouTubeCommercialVideo(video_id)

        elif video_type == VideoFactory.VIDEO_TYPE_TUTORIAL:
            return YouTubeTutorialVideo(video_id)

        else:
            raise ValueError('Invalid video type {}'.format(video_type))


class SiteTwoVideoFactory(VideoFactory):
    """
    This site hosts its videos on Vimeo
    """
    def create_video(self, video_type, video_id):
        if video_type == VideoFactory.VIDEO_TYPE_COMMERCIAL:
            return VimeoCommercialVideo(video_id)

        elif video_type == VideoFactory.VIDEO_TYPE_TUTORIAL:
            return VimeoTutorialVideo(video_id)

        else:
            raise ValueError('Invalid video type {}'.format(video_type))


# Entities

class AbstractVideo:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_video_data(self):
        pass


class YouTubeCommercialVideo(AbstractVideo):
    def __init__(self, video_id, *args, **kwargs):
        self._video_src = 'http://www.youtube.com/?watch={}'.format(video_id)

        super(YouTubeCommercialVideo, self).__init__(*args, **kwargs)

    def get_video_data(self):
        return {'video_type': 'commercial', 'provider': 'Youtube', 'src': self._video_src}


class YouTubeTutorialVideo(AbstractVideo):
    def __init__(self, video_id, *args, **kwargs):
        self._video_src = 'http://www.youtube.com/?watch={}'.format(video_id)

        super(YouTubeTutorialVideo, self).__init__(*args, **kwargs)

    def get_video_data(self):
        return {'video_type': 'tutorial', 'provider': 'Youtube', 'src': self._video_src}


class VimeoCommercialVideo(AbstractVideo):
    def __init__(self, video_id, *args, **kwargs):
        self._video_src = 'http://www.vimeo.com/?watch={}'.format(video_id)

        super(VimeoCommercialVideo, self).__init__(*args, **kwargs)

    def get_video_data(self):
        return {'video_type': 'commercial', 'provider': 'Vimeo', 'src': self._video_src}


class VimeoTutorialVideo(AbstractVideo):
    def __init__(self, video_id, *args, **kwargs):
        self._video_src = 'http://www.vimeo.com/?watch={}'.format(video_id)

        super(VimeoTutorialVideo, self).__init__(*args, **kwargs)

    def get_video_data(self):
        return {'video_type': 'tutorial', 'provider': 'Vimeo', 'src': self._video_src}


# Create videos for site one and site two
if __name__ == "__main__":
    site_one_factory = SiteOneVideoFactory()
    site_two_factory = SiteTwoVideoFactory()

    # SiteOne
    commercial_video = site_one_factory.create_video(VideoFactory.VIDEO_TYPE_COMMERCIAL, '123commercialid')
    tutorial_video = site_one_factory.create_video(VideoFactory.VIDEO_TYPE_TUTORIAL, '123tutorialid')

    print 'SiteOne videos:'
    print commercial_video.get_video_data(), tutorial_video.get_video_data()

    # SiteTwo
    commercial_video = site_two_factory.create_video(VideoFactory.VIDEO_TYPE_COMMERCIAL, '123commercialid')
    tutorial_video = site_two_factory.create_video(VideoFactory.VIDEO_TYPE_TUTORIAL, '123tutorialid')

    print 'SiteTwo videos:'
    print commercial_video.get_video_data(), tutorial_video.get_video_data()


### OUTPUT ###
# SiteOne videos:
# {'src': 'http://www.youtube.com/?watch=123commercialid', 'video_type': 'commercial', 'provider': 'Youtube'} {'src': 'http://www.youtube.com/?watch=123tutorialid', 'video_type': 'tutorial', 'provider': 'Youtube'}
# SiteTwo videos:
# {'src': 'http://www.vimeo.com/?watch=123commercialid', 'video_type': 'commercial', 'provider': 'Vimeo'} {'src': 'http://www.vimeo.com/?watch=123tutorialid', 'video_type': 'tutorial', 'provider': 'Vimeo'}
