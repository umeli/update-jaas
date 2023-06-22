import sys

authList = [
    {'alias': 'activitiesJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'blogsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'commonJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'communitiesJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'dogearJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'filesJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'filesSignatureJAAS', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'forumsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'homepageJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'icecJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'metricsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'metricseventcaptureJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'metricsuiJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'mobileJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'newsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'profilesJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'pushnotificationJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'searchJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'urlpreviewJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'widgetcontainerJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'wikisJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'DocsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'},
    {'alias': 'essappsJAASAuth', 'pw': 'PASSWORD', 'user': 'LCUSER'}
]


for auth in authList:
    print "update Password for %s / %s" % (auth["alias"], auth["user"])
    try:
        AdminTask.modifyAuthDataEntry(
            ['-alias', auth["alias"], '-user', auth["user"], '-password', auth["pw"]])
    except:
        print "********"
        print "could not update %s" % (auth["alias"])
        print "********"
        print sys.exc_info()[0]
