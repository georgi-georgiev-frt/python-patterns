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
    """
    Defining an interface for creating single object. Let subclasses decide what class to instantiate.
    https://github.com/georgi-georgiev-frt/python-patterns#abstract-factory-vs-factory-method-patterns-whats-the-difference
    """
    VIDEO_TYPE_COMMERCIAL = 'commercial'
    VIDEO_TYPE_TUTORIAL = 'tutorial'

    def __init__(self):
        pass

    def create_video(self, video_type, video_src):
        """
        :rtype AbstractVideo
        """
        raise NotImplementedError


class SiteOneVideoFactory(VideoFactory):
    """
    This site hosts its videos on Youtube
    """

    def create_video(self, video_type, video_id):
        if video_type == VideoFactory.VIDEO_TYPE_COMMERCIAL:
            video = YouTubeVideo(video_id, video_type)
            # Perform commercial video creational tasks
            video.set_is_commercial(True)  # Not really best example for creational task
            video.set_is_tutorial(False)  # Neither this one, but you got the idea :)

        elif video_type == VideoFactory.VIDEO_TYPE_TUTORIAL:
            video = YouTubeVideo(video_id, video_type)
            # Performing tutorial video creational tasks
            video.set_is_commercial(False)
            video.set_is_tutorial(True)

        else:
            raise ValueError('Invalid video type {}'.format(video_type))

        return video


class SiteTwoVideoFactory(VideoFactory):
    """
    This site hosts its videos on Vimeo
    """
    def create_video(self, video_type, video_id):
        if video_type == VideoFactory.VIDEO_TYPE_COMMERCIAL:
            video = VimeoVideo(video_id, video_type)
            # Performing commercial video creational tasks
            video.set_is_commercial(True)
            video.set_is_tutorial(False)

        elif video_type == VideoFactory.VIDEO_TYPE_TUTORIAL:
            video = VimeoVideo(video_id, video_type)
            # Performing tutorial video creational tasks
            video.set_is_commercial(False)
            video.set_is_tutorial(True)

        else:
            raise ValueError('Invalid video type {}'.format(video_type))

        return video


# Entities

class AbstractVideo:
    __metaclass__ = ABCMeta

    def __init__(self, video_type):
        self._is_commercial = False
        self._is_tutorial = False
        self._video_type = video_type

    @abstractmethod
    def get_video_data(self):
        pass

    def set_is_commercial(self, is_commercial):
        self._is_commercial = is_commercial

    def set_is_tutorial(self, is_tutorial):
        self._is_tutorial = is_tutorial


class YouTubeVideo(AbstractVideo):
    def __init__(self, video_id, video_type):
        self._video_src = 'http://www.youtube.com/?watch={}'.format(video_id)

        super(YouTubeVideo, self).__init__(video_type)

    def get_video_data(self):
        return {'video_type': self._video_type, 'provider': 'Youtube', 'src': self._video_src}


class VimeoVideo(AbstractVideo):
    def __init__(self, video_id, video_type):
        self._video_src = 'http://www.vimeo.com/?watch={}'.format(video_id)

        super(VimeoVideo, self).__init__(video_type)

    def get_video_data(self):
        return {'video_type': self._video_type, 'provider': 'Vimeo', 'src': self._video_src}


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
