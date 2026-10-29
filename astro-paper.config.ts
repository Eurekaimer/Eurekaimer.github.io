import { defineAstroPaperConfig } from "./src/types/config";

export default defineAstroPaperConfig({
  site: {
    url: "https://www.eurekaimer.icu",
    title: "Eurekaimer",
    description: "A quiet personal homepage.",
    author: "Eurekaimer",
    profile: "https://github.com/Eurekaimer",
    ogImage: "profile.jpg",
    lang: "en",
    timezone: "Asia/Shanghai",
    dir: "ltr",
  },
  posts: {
    perPage: 4,
    perIndex: 0,
    scheduledPostMargin: 15 * 60 * 1000,
  },
  features: {
    lightAndDarkMode: true,
    dynamicOgImage: false,
    showArchives: false,
    showBackButton: true,
    editPost: {
      enabled: false,
    },
    search: false,
  },
  socials: [
    {
      name: "github",
      url: "https://github.com/Eurekaimer",
      linkTitle: "Eurekaimer on GitHub",
    },
    {
      name: "wechat",
      url: "https://img.eurekaimer.icu/objects/default/b463e505-e743-4907-9ec6-9eba211aa5fb.webp",
      linkTitle: "WeChat QR code",
    },
    {
      name: "bilibili",
      url: "https://space.bilibili.com/702046230?spm_id_from=333.1007.0.0",
      linkTitle: "Eurekaimer on Bilibili",
    },
    {
      name: "qq",
      url: "https://img.eurekaimer.icu/objects/default/a69390b0-3e05-41d0-906f-9ae66a96dd72.webp",
      linkTitle: "QQ QR code",
    },
    {
      name: "mail",
      url: "mailto:2507983039@qq.com",
      linkTitle: "Email Eurekaimer",
    },
  ],
  shareLinks: [],
});

