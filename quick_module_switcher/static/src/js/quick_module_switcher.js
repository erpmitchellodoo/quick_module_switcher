/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class QuickModuleSwitcher extends Component {
    setup() {
        this.menuService = useService("menu");
        this.orm = useService("orm");
        this.state = useState({ menuIds: [] });

        onWillStart(async () => {
            this.state.menuIds = await this.orm.call(
                "res.users",
                "get_quick_switch_menu_ids",
                []
            );
        });
    }

    get shortcuts() {
        const selectedMenuIds = new Set(this.state.menuIds);
        return this.menuService.getApps().filter((app) => selectedMenuIds.has(app.id));
    }

    getAppIconSrc(app) {
        if (!app.webIconData) {
            return "/web/static/img/default_icon_app.png";
        }
        if (app.webIconData.startsWith("data:image") || app.webIconData.startsWith("/")) {
            return app.webIconData;
        }
        const mimeType = app.webIconData.startsWith("P") ? "image/svg+xml" : "image/png";
        return `data:${mimeType};base64,${app.webIconData.replace(/\s/g, "")}`;
    }

    async onSelectShortcut(app) {
        await this.menuService.selectMenu(app);
    }
}

QuickModuleSwitcher.template = "quick_module_switcher.QuickModuleSwitcher";
QuickModuleSwitcher.components = { Dropdown, DropdownItem };

registry.category("systray").add(
    "quick_module_switcher.QuickModuleSwitcher",
    { Component: QuickModuleSwitcher },
    { sequence: 45 }
);
