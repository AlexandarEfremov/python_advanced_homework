from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."
        inf_username = next((i for i in self.influencers if i.username == username), None)
        if inf_username:
            return f"{username} is already registered."
        inf = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(inf)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."
        camp = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if camp:
            return f"Campaign ID {campaign_id} has already been created."
        new_campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        inf = next((i for i in self.influencers if i.username == influencer_username), None)
        if inf is None:
            return f"Influencer '{influencer_username}' not found."
        camp = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)
        if camp is None:
            return f"Campaign with ID {campaign_id} not found."
        eligible_influencer = camp.check_eligibility(inf.engagement_rate)
        if eligible_influencer is False:
            return (f"Influencer '{influencer_username}' does not meet the eligibility criteria "
                    f"for the campaign with ID {campaign_id}.")
        payment_for_influencer = inf.calculate_payment(camp)
        if payment_for_influencer > 0.0:
            camp.approved_influencers.append(inf)
            camp.budget -= payment_for_influencer
            inf.campaigns_participated.append(camp)
            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")