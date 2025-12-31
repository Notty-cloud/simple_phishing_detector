"""
Suspicious keywords commonly found in phishing/spam emails
"""

# Keywords that suggest urgency or threats
URGENT_KEYWORDS = [
    'urgent', 'immediately', 'act now', 'limited time',
    'expires', 'deadline', 'hurry', 'quick', 'fast'
]

# Keywords related to account security
SECURITY_KEYWORDS = [
    'verify', 'confirm', 'suspended', 'locked', 'unusual activity',
    'security alert', 'unauthorized', 'blocked', 'compromised'
]

# Keywords promising rewards or money
FINANCIAL_KEYWORDS = [
    'prize', 'winner', 'congratulations', 'free', 'bonus',
    'cash', 'million', 'lottery', 'inheritance', 'claim'
]

# Action-oriented keywords
ACTION_KEYWORDS = [
    'click here', 'click below', 'update now', 'download',
    'open attachment', 'verify account', 'confirm identity'
]

# Personal information requests
PERSONAL_INFO_KEYWORDS = [
    'password', 'social security', 'bank account', 'credit card',
    'ssn', 'pin', 'account number', 'routing number'
]

# Combine all keywords into one master list
ALL_SUSPICIOUS_KEYWORDS = (
    URGENT_KEYWORDS + 
    SECURITY_KEYWORDS + 
    FINANCIAL_KEYWORDS + 
    ACTION_KEYWORDS + 
    PERSONAL_INFO_KEYWORDS
)

def get_all_keywords():
    """Returns the complete list of suspicious keywords"""
    return ALL_SUSPICIOUS_KEYWORDS

def get_keywords_by_category():
    """Returns keywords organized by category"""
    return {
        'urgent': URGENT_KEYWORDS,
        'security': SECURITY_KEYWORDS,
        'financial': FINANCIAL_KEYWORDS,
        'action': ACTION_KEYWORDS,
        'personal_info': PERSONAL_INFO_KEYWORDS
    }
