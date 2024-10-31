from django.utils.translation import gettext_lazy as _

PAGINATION_PERPAGE=10
UAE_TIMEZONE = 'Asia/Dubai'

# STOCK TYPE 
POPULAR = 1
FOREX = 2
ENERGIES = 3 
INDICES = 4
COMMODITIES = 5
SHARES = 6
STOCK_TYPE = ((POPULAR,_('Popular')),(FOREX,_('Forex')),(COMMODITIES,_('Commodities')),(INDICES,_('Indices')),(ENERGIES,_('Energies')),(SHARES,_('Shares')))

# MENU CACHE
MENU_CACHE_TIMEOUT = 60 * 60 * 24 # 1 day timeout
FOOTER_CACHE_TIMEOUT = 60 * 60 * 24 # 1 day timeout
#Folder structure for next js

FRONTEND_FOLDERS = [
	    ('servicepage', 'services',),
        ('productpage', 'products',),
        ('tradingpage', 'trading',),
        ('otherpage', '',),
        ('webinarpage', 'learning-hub',),
        ('workshoppage', 'learning-hub',),
        ('marketupdatepage', 'learning-hub',),
        ('technicalanalysispage', 'learning-hub',),
        ('economicreportpage', 'learning-hub',),
        ('pressreleasepage', 'learning-hub',),
        ('activitypage', 'learning-hub',),
        ('awardpage', 'learning-hub',),
        ('learningcontentpage', 'learning-hub',),
        ('blogindexpage', 'learning-hub',),
        ('webinarindexpage', 'learning-hub',),
        ('economicreportindexpage', 'learning-hub',),
        ('technicalanalysisindexpage', 'learning-hub',),
        ('marketupdateindexpage', 'learning-hub',),
        ('workshopindexpage', 'learning-hub',),
        ('pressreleaseindexpage', 'learning-hub',),
        ('activityindexpage', 'learning-hub',),
        ('awardindexpage', 'learning-hub',),
        ('partnershippage', 'partnership',),

    ]


#api urls corresponding to models
API_URLS = [
	    ('aboutpage', 'about-us/',),
        # ('servicepage', 'service/',),
        # ('tradingpage', 'trading/',),
        # ('productpage', 'product/',),
        # ('partnershippage','partnership/',),
        # ('otherpage','secondary-pages/',),
        # ('learningcontentpage','learning-hub/page/',),
        # ('learninglinkpage','learning-hub/link-page/',),        
        # ('blogindexpage', 'learn-to-invest/',),
        # ('webinarindexpage', 'webinars/',),
        # ('economicreportindexpage', 'economic-reports/',),
        # ('technicalanalysisindexpage', 'technical-analysis/',),
        # ('marketupdateindexpage', 'market-updates/',),
        # ('workshopindexpage', 'workshop/',),
        # ('pressreleaseindexpage', 'press-release/',),
        # ('activityindexpage', 'activities/',),
        # ('awardindexpage', 'awards/',),
    ]

BLOG_MODELS = ['webinarindexpage',
                'economicreportindexpage',
                'technicalanalysisindexpage', 
                'marketupdateindexpage',
                'workshopindexpage', 
                'pressreleaseindexpage', 
                'activityindexpage',
                'awardindexpage',
                'blogindexpage']

ALL_PAGE_TARGETS = ['about.AboutPage',
                        'activities.ActivityIndexPage',
                        'awards.AwardIndexPage', 
                        'blog.BlogIndexPage', 
                        'economic_reports.EconomicReportIndexPage',
                        'market_updates.MarketUpdateIndexPage',
                        'other_pages.OtherPage',
                        'partnership.PartnershipPage',
                        'press_release.PressReleaseIndexPage',
                        'products.ProductPage',
                        'services.ServicePage',
                        'technical_analysis.TechnicalAnalysisIndexPage',
                        'trading.TradingPage',
                        'webinar.WebinarIndexPage',
                        'workshop.WorkshopIndexPage',
                        'learning_hub.LearningContentPage',
                        'learning_hub.LearningLinkPage']

PAGE_TARGETS = [
                    'Course.CoursePage',
                    # 'other_pages.OtherPage',
                    # 'partnership.PartnershipPage',
                    # 'products.ProductPage',
                    # 'services.ServicePage',
                    # 'trading.TradingPage',
                    # 'learning_hub.LearningContentPage',
                    # 'learning_hub.LearningLinkPage'
                    ]

BLOG_INDEX_TARGETS = ['technical_analysis.TechnicalAnalysisIndexPage', 
                        'market_updates.MarketUpdateIndexPage', 
                        'economic_reports.EconomicReportIndexPage',
                        'webinar.WebinarIndexPage',
                        'workshop.WorkshopIndexPage',
                        'press_release.PressReleaseIndexPage',
                        'activities.ActivityIndexPage',
                        'awards.AwardIndexPage',
                        'blog.BlogIndexPage']

BLOG_TARGETS = [
        'technical_analysis.TechnicalAnalysisPage',
        'webinar.WebinarPage',
        'economic_reports.EconomicReportPage',
        'market_updates.MarketUpdatePage',
        'workshop.WorkshopPage',
        'press_release.PressReleasePage',
        'activities.ActivityPage',
        'awards.AwardPage',
    ]
CARD_CHOICES = [
	    ('2', _('2 cards per row'),),
        ('3', _('3 cards per row'),),
        ('4', _('4 cards per row'),),
    ]
    
BG_CHOICES = [
        ('transparent', _('Transparent Background'),),
	    ('solid', _('Solid Background'),),        
        ('gradient', _('Gradient Background'),),
        ('pattern', _('Pattern Background'),),
    ]

TOP_PADDING_CHOICES = [
        ('big', _('Big (120px/80px/40px)'),),
	    ('small', _('Small (64px)'),),        
        ('none', _('NO Padding'),),
    ]

BOTTOM_PADDING_CHOICES = [
        ('big', _('Big (120px/80px/40px)'),),
	    ('small', _('Small (64px)'),),        
        ('none', _('NO Padding'),),  
    ]

IMAGE_LAYOUT = [
        ('overlay', _('Overlayed Image)'),),
	    ('default', _('Plain Image'),),       
    ]

ALIGNMENT_CHOICES = [
        ('center', _('Center'),),
	    ('right', _('Right'),),        
        ('left', _('Left'),),
    ]

# Define a list of social media options
SOCIAL_MEDIA_CHOICES = [
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('linkedin', 'LinkedIn'),
    ('instagram', 'Instagram'),
    ('youtube', 'YouTube'),
    # Add more as needed
]

# This map corresponds to the choices in your VideoBlock
PROFICIENCY_LEVEL_CHOICES = [
    ('beginner', _('Beginner'),),
    ('intermediate', _('Intermediate'),),
    ('advanced', _('Advanced'),),
]

TRADE_FORM_TYPES = [
    ('MT4','MT4'),
    ('MT5','MT5'),
    ('GTN','GTN'),
]

OTHER_FORM_TYPES = [
    ('CONTACT','CONTACT'),
    ('ENQUIRY','ENQUIRY'),
    ('REQUEST_DEMO','REQUEST DEMO')
]